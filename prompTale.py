from transformers import pipeline, set_seed

from story.models import StoryBook, Image, TextEntry

from django.core.files import File
from diffusers import StableDiffusionPipeline
import torch
import os
from django.conf import settings
from textGenerator import generateText

model2_id = "runwayml/stable-diffusion-v1-5"

if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")

pipe = StableDiffusionPipeline.from_pretrained(model2_id, torch_dtype=torch.float16)
pipe.to("mps")


def generateImages(prompts):

    # temporary storage
    image_paths = []
    for i in range(len(prompts)):
        image = pipe(prompts[i]+', animated').images[0] 
        image_dir = os.path.join(settings.MEDIA_ROOT, 'images')   
        image_path = os.path.join(image_dir, f'raw{i}.jpg')
        image.save(image_path)
        image_paths.append(image_path)

    # saving images in db
    images = []
    for path in image_paths:
        with open(path, 'rb') as f:
            new_image = Image()
            new_image.image.save(os.path.basename(path), File(f))
            new_image.save()
            images.append(new_image)
    return images

    
def generateStory(prompt, user):
    story_book = StoryBook(
		username = user,
		is_public=False
		)
    story_book.save()

    
    response_text = generateText(prompt)

    pages = response_text['text']
    title = response_text['title']
    genre = response_text['genre']
    image_prompts = response_text['prompts']
 
    for page in pages:
        story_book.text.add(TextEntry.objects.create(text=page))

    gen_images = generateImages(image_prompts)      

    for image in gen_images:
        story_book.images.add(image)
    story_book.title = title
    story_book.description = genre
    story_book.save()

    return story_book.id
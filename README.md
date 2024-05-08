
#  PrompTale
# Project Overview
## Objective:
The objective of "PromptTale" is to create a software capable of making and illustrating compelling stories, aiming to reignite people's passion for reading and storytelling. By providing stories and illustrations tailored to individual tastes, "PromptTale" seeks to revolutionize the reading and storytelling experience, offering a new way to engage with and enjoy stories on demand.

## Introduction:
"PromptTale" is a visionary project that seeks to transform the world of storytelling by harnessing the power of technology. In a time where digital content is abundant, "PromptTale" stands out as a unique platform that not only delivers stories catered to individual preferences but also enhances them with captivating illustrations.
This software is designed for a wide audience, including students, readers, writers, and teachers, offering them a novel way to experience and create stories. With a focus on user engagement and satisfaction, "PromptTale" aims to provide an immersive storytelling experience that captivates and inspires.
Through innovative features such as user-generated prompts and fully illustrated stories, "PromptTale" aims to rekindle the joy of reading and storytelling, making it more accessible and enjoyable for everyone. Join us on this journey as we embark on a mission to ignite the passion for stories and bring imagination to life.

## Problem Statement
The decline in active book readership and the stagnation in the evolution of storytelling pose significant challenges to the literary world. Traditional methods of storytelling may fail to captivate modern audiences, leading to disengagement and disinterest in reading. Moreover, the lack of personalized content tailored to individual preferences further exacerbates this issue. PromptTale addresses these challenges by offering a novel solution that combines AI-generated stories with illustrations, delivering unique and engaging content to users.

## Project Scope
PromptTale's scope encompasses the development of a robust software application capable of generating full-length stories with accompanying illustrations. This project requires collaboration among team members with expertise in AI, ML, software development, and user interface design. The software will allow users to create accounts, customize their profiles, and interact with the story generation system through prompts and preferences. Additionally, PromptTale will offer features such as storybook management, customization options, and privacy settings to enhance user experience and engagement.

## 1. Tools and Technologies
To bring PromptTale to life, we will utilize a range of tools and technologies, including:

#### Artificial Intelligence: 
Primarily, we will leverage AI language models for text generation and image generation tools such as Stable Diffusion.

#### Machine Learning Frameworks:
 We will employ ML frameworks like Torch for model training and deployment.
#### Development Tools: 
Visual Studio Code will serve as our primary integrated development environment (IDE) for coding tasks.
#### Programming Languages: 
Python will be the primary programming language for backend development, with HTML, CSS, and JavaScript used for frontend development.
#### Web Framework: 
Django will provide the foundational framework for building the web application.
#### External APIs: 
We will integrate with OpenAI's language model API for text generation tasks.

## 2. Differentiation from Existing Projects
While projects like ChatGPT utilize AI language models for text generation, PromptTale distinguishes itself by focusing specifically on storytelling. Unlike generic chatbots, PromptTale's AI model is tailored to understand narrative structures and generate cohesive stories with logical consistency. Additionally, the integration of image generation tools enhances the storytelling experience by providing visual representations aligned with the generated stories.

## 3.  Project Details

### User Experience
#### Account Management
Users can create accounts, log in, and edit their profiles, including details such as email, username, and profile picture.

#### Story Creation
Users have the ability to create storybooks by describing characters, themes, and genres through user prompts. These prompts serve as inputs for the AI model to generate full-length stories.

#### Storybook Customization
Users can customize their storybooks by selecting colors, fonts, and styles, personalizing the reading experience to their preferences.

#### Privacy Settings
PromptTale offers options for users to make their storybooks public or private, allowing authors to control the visibility of their content.

### User Interface
#### Home Interface
The home interface displays storybooks in card format, with hover functionality to reveal details. It includes buttons for signing up, logging in, and accessing user profiles.

#### Account Creation Interface
Users can create accounts by providing email, username, password, and password confirmation. Clear error messages are displayed for invalid inputs.

#### Login Interface
The login interface prompts users to enter their email and password, with options for forgot password and account creation.

#### Update Profile
Users can update their profiles by modifying username, email, old password, and new password. Error messages are displayed for existing usernames or emails.

#### Story Creation Interface
The story creation interface allows users to input prompts for generating stories. A "create" button initiates the story generation process.

#### Story Book Management Interface
Users can manage their storybooks, with functions to make stories public or private, edit, or delete them. Clear visual cues distinguish between public and private stories.

## 4. System Interfaces
#### Hardware Interfaces
PromptTale interacts with standard hardware components such as keyboards, mice, and displays, typical for web-based applications.

#### Software Interfaces
Integration with OpenAI's language model API enables text generation, while image generation tools like Stable Diffusion produce illustrations based on story prompts. A database system stores user account information, story prompts, generated stories, and ratings.

## 5. System Features
#### Input User Prompt
Users input prompts to generate stories, initiating the AI-based story generation process.

#### Log In / Sign Up
User authentication is required for accessing features such as saving generated stories. After logging in, users can navigate the software's functionalities.
#### Save and Manage Stories
Users can save their generated stories and manage them, including editing, deleting, or sharing them with others.

#### Storybook Customization
Users can customize the appearance of their storybooks, including fonts, colors, and layout, to create a personalized reading experience.

#### Public and Private Storybooks
Users can choose to make their storybooks public, allowing others to read and enjoy them, or keep them private for personal use only.

#### Story Rating and Feedback
Users can rate stories they've read and provide feedback, helping to improve the quality of generated stories and provide valuable insights for authors.

## 6. Nonfunctional Requirements
Performance Requirements
The AI story generator should process and generate stories within milliseconds, ensuring a seamless user experience. Response times should be within 100 milliseconds under normal conditions, with scalability to accommodate increasing loads.

#### Safety Requirements
PromptTale must prevent the generation of content promoting violence, hate speech, or discrimination. Security mechanisms should detect and prevent breaches or unauthorized access to data, ensuring compliance with data protection regulations.

#### Software Quality Attributes
Reliability, usability, maintainability, adaptability, and robustness are prioritized to deliver a high-quality user experience. The system should handle unexpected inputs or errors gracefully, without compromising integrity.

#### Business Rules
Only registered users can access features like saving generated stories. Users must agree to terms of service and privacy policies. Commercial use of generated stories may require additional licensing or permissions.

## 7. Detailed Analysis

### Dataset and Features
PromptTale does not rely on a traditional dataset but instead utilizes AI language models and image generation tools for content creation. The dataset consists of user prompts, story prompts, generated stories, and associated illustrations.

### Feature Selection
Feature selection is not applicable in the context of PromptTale as the focus is on generating stories based on user prompts rather than traditional feature-based analysis.

### Model Training
PromptTale utilizes pre-trained AI language models, such as GPT, for text generation tasks. These models are fine-tuned on a corpus of storytelling data to ensure coherence and relevance in generated stories. For image generation, tools like Stable Diffusion are employed to produce illustrations corresponding to the generated stories.

### Evaluation Metrics
Evaluation of PromptTale's performance revolves around user satisfaction and engagement metrics rather than traditional ML evaluation metrics. User feedback, story ratings, and retention rates are key indicators of the software's success.

## Analysis and Insights

#### Dataset Exploration
The dataset provided a comprehensive overview of various attributes related to storytelling, including user prompts, story themes, and generated content. Exploring this dataset revealed insights into user preferences, popular genres, and common story elements.

#### User Preferences
Analysis of user prompts and generated stories highlighted recurring themes and genres preferred by users. Horror, fantasy, and mystery emerged as popular genres, indicating a diverse range of storytelling interests among users.

#### Content Generation
The AI-based content generation process demonstrated its capability to produce compelling stories tailored to user prompts. By leveraging language models and image generation tools, PromptTale successfully created immersive narratives accompanied by visually appealing illustrations.

#### Engagement Metrics
Monitoring user interactions and engagement metrics provided valuable insights into the platform's performance and user satisfaction. Metrics such as story views, ratings, and user feedback helped evaluate the effectiveness of generated content and identify areas for improvement.

### Conclusion

PromptTale represents a significant advancement in AI-driven storytelling, offering users a personalized and immersive reading experience. By harnessing the power of AI language models and image generation techniques, PromptTale delivers compelling stories tailored to individual preferences. Through continuous iteration and user feedback, PromptTale aims to redefine the landscape of digital storytelling, inspiring creativity and fostering a vibrant community of writers and readers.



### Dataset
In Promptale, a versatile AI-powered storytelling platform, the core functionality revolves around generating engaging stories tailored to users' preferences. This process involves three key components: text generation using GPT (Generative Pre-trained Transformer), image generation using Stable Diffusion, and text evaluation using Sentence Transformers. Let's delve into each aspect in detail:

#### Text Generation using GPT:
Promptale utilizes GPT, a state-of-the-art language model, to generate textual content based on user prompts. The dataset for training the GPT model encompasses a diverse range of textual data, including literature, stories, articles, and story prompts paired with continuations. This dataset enables GPT to understand language nuances, context, and narrative structures, empowering it to produce coherent and immersive stories in response to user prompts, to ensure a broad understanding of language and storytelling.

#### Image Generation using Stable Diffusion:
To complement the generated stories, Promptale employs Stable Diffusion for image generation. The dataset for training the Stable Diffusion model consists of a wide array of images sourced from various repositories, including stock photo websites and custom-created visuals. This dataset covers diverse visual content, such as scenes, objects, characters,settings, various types of images, such as illustrations, photographs, or even abstract art, to provide a wide range of visual styles for the model to learn from.  By training on this dataset, Stable Diffusion learns to produce high-quality, contextually relevant images that enhance the storytelling experience. 

#### Text Evaluation using Sentence Transformers:
To ensure the quality and relevance of generated stories, Promptale incorporates Sentence Transformers for text evaluation. The dataset for training and evaluating Sentence Transformers depends on the specific tasks it performs. For tasks like semantic textual similarity, the dataset contains sentence pairs with corresponding similarity scores. For text classification, the dataset comprises labeled text data across various categories. By training on such datasets, Sentence Transformers gain the ability to understand semantic relationships between sentences and accurately classify text based on content.

By leveraging these three components in tandem, Promptale delivers a comprehensive storytelling experience tailored to users' preferences. Users can input prompts, and the system generates immersive stories accompanied by relevant illustrations. The integration of GPT, Stable Diffusion, and Sentence Transformers ensures that the generated content is not only coherent and engaging but also contextually relevant and of high quality.

In conclusion, Promptale revolutionizes storytelling by harnessing the power of AI to create personalized and captivating narratives. Through sophisticated text and image generation techniques, coupled with advanced text evaluation capabilities, Promptale sets a new standard for immersive storytelling experiences.



## 8. How To Use

Open this folder in VS Code and start a new terminal.

### pre requisites

Any apple pc with M1 chip or above is required for this, because this project uses features only available to the M1 mac and above.

### libraries and other requirements

For this project you will need:

- python3.9, other versions may cause issues. (run command pip install python3.9)
- Django, this is needed for database handling. (run command pip install django)
- openai, this is needed to generate the story text and image prompts (run command pip install openai)
- torch, needed to create any neural networks and other services (run command pip install torch)
- transformers, used to clean, reduce, expand features (run command pip install transformers)              
- pillow, needed for manipulating and processing images (run command pip install pillow)
- accelerate, to allow pytorch code to be run across distributed configuration (run command pip install accelerate)                   
- diffusers, needed for AI based image generation (run command pip install diffusers)
- scentence_transformers, to compute embeddings (dense vector representations) for sentences (run command pip install scentence_transformers)

### setup

Run the following commands on the terminal, **IN ORDER**:

- python3.9 -m venv venv 
- source venv/bin/activate
- cd src
- python3.9 manage.py runserver

### open website

After running the command **python3.9 manage.py runserver**, your pc will check for system files, requirements and present you with a link, open it using command + click.

### admin panel access

The link provided by the execution of **python3.9 manage.py runserver** can be appended with /admin to access the admin panel. 
e.g: <link>/admin


## 9. Why Use These APIs

### Stable Diffuse for Image Generation

There are several pretrained models for image generation, each with its own strengths and characteristics. Some popular ones include:

- **StyleGAN and StyleGAN2**: StyleGAN and its improved version, StyleGAN2, are known for their ability to generate high-quality and diverse images, particularly faces. They are widely used in artistic and creative applications.
- **BigGAN**: BigGAN is designed for generating high-resolution images and is known for its ability to produce images with high fidelity and diversity.
- **CLIP (Contrastive Language-Image Pretraining)**: While not strictly an image generation model, CLIP can be used for text-to-image generation by aligning text prompts with images in a latent space. It is known for its ability to generate images based on natural language descriptions.
- **VQ-VAE-2 (Vector Quantized Variational Autoencoder)**: VQ-VAE-2 is a generative model that can be used for image generation. It is known for its ability to generate high-quality images with rich details.
- **DALL-E**: DALL-E is a transformer-based model designed for generating images from textual descriptions. It is known for its ability to generate creative and diverse images based on textual prompts.

Stable Diffusion, on the other hand, is chosen for image generation tasks because of its unique approach and advantages:

- **Progressive Generation**: Stable Diffusion generates images in a progressive manner, which can lead to smoother and more coherent image generation compared to other methods.
- **Controlled Generation**: Stable Diffusion allows for controlled image generation by varying the diffusion process, enabling users to influence the style, content, and appearance of the generated images.
- **High-Quality Results**: Stable Diffusion is known for its ability to generate high-quality and realistic images with fine details, making it suitable for a wide range of applications.
- **Flexibility**: Stable Diffusion can be used for various image generation tasks, including generating images from text prompts, modifying existing images, and creating new images from scratch.

Overall, Stable Diffusion is chosen for image generation tasks because of its unique approach, which allows for controlled and high-quality image generation, making it suitable for a wide range of applications, from artistic creation to data augmentation in machine learning.

### Chat GPT 3.5 Turbo for text generation and image prompt generation

There are several pretrained models available for generating text, each with its own strengths and characteristics. Here are some popular ones:

1. **GPT-3** (Generative Pre-trained Transformer 3)*: GPT-3 is one of the largest and most powerful language models, capable of generating human-like text across a wide range of topics and styles. It is known for its ability to produce coherent and contextually relevant responses.
2. **GPT-2**: GPT-2 is the predecessor to GPT-3 and is also capable of generating high-quality text, although with fewer parameters and a slightly lower performance level compared to GPT-3.
3. **BERT (Bidirectional Encoder Representations from Transformers)**: While BERT is primarily used for understanding and classifying text, it can also be fine-tuned for text generation tasks. However, its performance in text generation may not be as strong as models specifically designed for that purpose.
4. **T5 (Text-to-Text Transfer Transformer)**: T5 is a transformer model that frames all NLP tasks as text-to-text tasks, where both inputs and outputs are in natural language format. It has shown strong performance across a variety of NLP tasks, including text generation.
5. **CTRL**: CTRL is a conditional transformer language model that allows for control over the style and content of the generated text. It is particularly useful for tasks where specific control over the output is required.

OpenAI ChatGPT-3.5 Turbo is a variant of GPT-3.5 that includes enhancements to improve its performance and capabilities, such as increased context window size and improved tokenization. It is chosen for text generation tasks because of its strong performance, ability to generate coherent and contextually relevant text, and its availability for developers through OpenAI's API. Additionally, OpenAI has provided tools and resources to help developers effectively use ChatGPT-3.5 Turbo for various text generation tasks.

### scentence_transformers for evaluation of text

There are several other pretrained models for evaluating text, each with its own strengths and weaknesses. Some popular ones include:

1. **BERT (Bidirectional Encoder Representations from Transformers)**: BERT is a powerful transformer-based model that considers context from both directions of a text sequence. It is widely used for various NLP tasks due to its effectiveness.

2. **RoBERTa (A Robustly Optimized BERT Approach)**: RoBERTa is an optimized version of BERT that improves performance by training for longer with more data and larger batch sizes.

3. **XLNet**: XLNet is another transformer-based model that uses a permutation language modeling objective, allowing it to capture bidirectional context more effectively.

4. **GPT (Generative Pre-trained Transformer)**: GPT models, including GPT-2 and GPT-3, are designed for generating text but can also be fine-tuned for text classification and other tasks.

5. **ALBERT (A Lite BERT)**: ALBERT is a "lightweight" version of BERT that reduces the number of parameters while maintaining performance, making it more efficient for certain applications.

6. **DistilBERT**: DistilBERT is a distilled version of BERT that retains most of its performance while using fewer parameters, making it faster and more resource-efficient.

Sentence Transformer is considered better than some of these models for text similarity and semantic search tasks because it is specifically designed to generate sentence embeddings that capture semantic meaning effectively. It is trained on a diverse range of tasks and datasets, which helps it generalize well to different text evaluation tasks. Additionally, Sentence Transformer allows for easy fine-tuning on specific datasets, making it adaptable to various applications. However, the choice of the best model depends on the specific task and the trade-offs between performance and efficiency that are acceptable for the application.

### Libraries

The project utilizes several libraries and frameworks to implement its functionalities:

- OpenAI GPT-3: A powerful language model for generating text-based content.
- Stable Diffusion: An image generation tool used to create illustrations based on generated stories.
- Django: A web framework for building the backend infrastructure of the PromptTale platform.
- Python: The primary programming language for developing the PromptTale application logic.
- HTML, CSS, and JavaScript: Frontend technologies for designing the user interface and enhancing user interactions.
- 
### References

- OpenAI. (n.d.). GPT-3: Language Models. Retrieved from https://openai.com/gpt-3
- Stable Diffusion. (n.d.). Image Generation. Retrieved from https://stablediffusion.com
- Django Documentation. (n.d.). Web Framework. Retrieved from https://docs.djangoproject.com/en/stable/
- Python Documentation. (n.d.). Programming Language. Retrieved from https://docs.python.org/3/
- Sentence Transformer. (n.d.). In GitHub. Retrieved Month Day, Year, from https://github.com/UKPLab/sentence-transformers
replace refernec too


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
![account](https://github.com/emanroshan/PrompTale/assets/140584428/a85334fa-104c-43a5-992f-368ed67d7974)
![flip cards](https://github.com/emanroshan/PrompTale/assets/140584428/cf4d96b8-d269-4e54-8f86-88f6aa108b74)

#### Account Creation Interface
Users can create accounts by providing email, username, password, and password confirmation. Clear error messages are displayed for invalid inputs.
![craete account](https://github.com/emanroshan/PrompTale/assets/140584428/2adcef55-e62e-4b81-840a-e5503d5606c0)

#### Login Interface
The login interface prompts users to enter their email and password, with options for forgot password and account creation.
![login](https://github.com/emanroshan/PrompTale/assets/140584428/f5dabb88-d046-4496-bc61-640199ed3713)


#### Update Profile
Users can update their profiles by modifying username, email, old password, and new password. Error messages are displayed for existing usernames or emails.
![edit-profile](https://github.com/emanroshan/PrompTale/assets/140584428/8ee609a4-ff46-4985-a045-d81d81c4c69d)

#### Story Creation Interface
The story creation interface allows users to input prompts for generating stories. A "create" button initiates the story generation process.
![prompt](https://github.com/emanroshan/PrompTale/assets/140584428/e1b05dca-647d-4a73-8218-10b03e6fc880)

#### Story Book Management Interface
Users can manage their storybooks, with functions to make stories public or private, edit, or delete them. Clear visual cues distinguish between public and private stories.
![customization](https://github.com/emanroshan/PrompTale/assets/140584428/34108874-bb8a-4c2e-b03a-2c7b0f0c001c)

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

### References

- OpenAI. (n.d.). GPT-3: Language Models. Retrieved from https://openai.com/gpt-3
- Stable Diffusion. (n.d.). Image Generation. Retrieved from https://stablediffusion.com
- Django Documentation. (n.d.). Web Framework. Retrieved from https://docs.djangoproject.com/en/stable/
- Python Documentation. (n.d.). Programming Language. Retrieved from https://docs.python.org/3/
- Sentence Transformers: Multilingual Sentence Embeddings using BERT / RoBERTa / XLM-RoBERTa & Co. with PyTorch. (n.d.). Retrieved from https://www.sbert.net/docs/pretrained_models.html#sentence-transformers.

### Dataset

The dataset used for this project consists of user prompts, story themes, and generated content, collected from PromptTale users. It includes various attributes such as prompt text, genre tags, story content, and user ratings.

### Libraries

The project utilizes several libraries and frameworks to implement its functionalities:

- OpenAI GPT-3: A powerful language model for generating text-based content.
- Stable Diffusion: An image generation tool used to create illustrations based on generated stories.
- Django: A web framework for building the backend infrastructure of the PromptTale platform.
- Python: The primary programming language for developing the PromptTale application logic.
- HTML, CSS, and JavaScript: Frontend technologies for designing the user interface and enhancing user interactions.
## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```



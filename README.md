### AI Background Image Removal

Remove background from any images using AI

##  App Demo

![ai_background_removal_demo_video](https://github.com/george-mountain/ai-background-image-removal/assets/19597087/5e607785-aa5d-4087-b7e1-9775c04c5d70)

---
# gettin started


Fork or Clone this repo:

git clone https://github.com/george-mountain/ai-background-image-removal.git


### AI model download
Download the model by cloning its repo:

git clone https://huggingface.co/briaai/RMBG-1.4

Copy the model.pth file from RMBG-1.4 to the backend folder

## Running the application

use the Makefile commands to run the apps
 1. build the docker images:

 ```
    make build
```
In case you do not have Make installed on your PC, you can as well use the command below to build the images:


 ```
    docker compose up --build -d --remove-orphans
```
2. run the docker containers

```
    make up-v
```

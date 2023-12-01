# NASA Mars Rover Photo Retrieval
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd

# Fetch data from the Mars Photo API 
api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=DEMO_KEY&sol=1000"
api_key = ""
sol = 170  # Martian Sol 
response = requests.get(f"{api_url}/rovers/perseverance/photos?sol={sol}&api_key={api_key}")
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data['photos'])


print(df)

# Display images 
def display_images(image_urls):
    fig, axes = plt.subplots(1, len(image_urls), figsize=(15, 5))

    for i, img_url in enumerate(image_urls):
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        axes[i].imshow(img)
        axes[i].axis('off')

    plt.show()

# Display the first three images in the DataFrame
image_urls = df['img_src'].head(4).tolist()
display_images(image_urls)

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_poke():
    poke_id = np.random.randint(1, 151)
    api_url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(api_url)
    poke_data = response.json()
    return poke_data['name'], poke_data['sprites']['front_default']

def load_image_matrix(sprite_url):
    image_response = requests.get(sprite_url)
    with open("sprite.png", "wb") as file:
        file.write(image_response.content)
    return plt.imread("sprite.png")

def extract_colors(poke_matrix):
    flat_pixels = poke_matrix.reshape(-1, 4)
    hex_colors = []
    for pixel in flat_pixels:
        alpha = pixel[3]
        if alpha > 0:
            r, g, b = (pixel[0:3] * 255).astype(int)
            hex_code = f"#{r:02x}{g:02x}{b:02x}"
            hex_colors.append(hex_code)
    return hex_colors

def count_colors(hex_colors):
    df = pd.DataFrame({'Color': hex_colors})
    return df['Color'].value_counts()

def plot_data(name, poke_matrix, colors):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"{name}'s palette", fontweight='bold')
    ax1.imshow(poke_matrix)
    ax1.axis('off') 
    colors.plot(kind='bar', ax=ax2, color=colors.index, edgecolor='black')
    ax2.set_title("Color ranking by pixel")
    ax2.set_ylabel("Number of Pixels")
    ax2.tick_params(axis='x', rotation=45)
    plt.show()

def main():
    name, sprite_url = get_poke()
    poke_matrix = load_image_matrix(sprite_url)
    hex_colors = extract_colors(poke_matrix)
    colors = count_colors(hex_colors)
    plot_data(name, poke_matrix, colors)

if __name__ == "__main__":
    main()
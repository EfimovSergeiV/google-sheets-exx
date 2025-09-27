```zsh
touch credentials.json


npx tailwindcss-cli init
npx nuxi@latest module add @vite-pwa/nuxt



```

```zsh
# config file
nano conf.ts

#
const cfg = {
    "BASE_URL": 'https://api.meinewelt.ru/',
}

export default cfg
```

### WEBP

```zsh
# convert with GIMP
sudo apt install gimp webp

# convert with ffmpeg
ffmpeg -i input.mp4 -vcodec libwebp -loop 0 -an -vsync 0 output.webp

# convert with webp (off google tools)
sudo apt install webp
img2webp frame*.png -o anim.webp
```
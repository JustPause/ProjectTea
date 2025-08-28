# Tea project, Tea database

This is a collaboration project between Nina, a designer, and Justinas, a programmer. We both share a deep passion for tea and want to share that love with the world, which is why we decided to create a website dedicated to tea enthusiasts like ourselves. Through our site, you'll be able to explore various types of teas, learn more about their origins, brewing techniques, and dive into the rich culture surrounding tea. We also share our personal tasting experiences and expert recommendations to help guide your own tea journey. Additionally, this project doubles as Justinas' college semester project, so he is putting in extra effort to ensure it’s completed before the New Year. We hope you’ll find our site as enjoyable to use as we have found creating it!

## Front-End

### inportant links

[vue integrasion](https://docs.astro.build/en/guides/integrations-guide/vue/)
[after finish setuo, configer astro ASAP](https://docs.astro.build/en/reference/configuration-reference/)
[add content pages for evry tea](https://docs.astro.build/en/guides/content-collections/)
[or pages](https://docs.astro.build/en/basics/astro-pages/)
[intresting conspet, need to inpelent](https://docs.astro.build/en/guides/view-transitions/)

[Work step by step on this](https://docs.astro.build/en/tutorial/2-pages/)

### ToDo

#### Pages's



#### Fetures

- [ ] try to add [boonakis-tea-api](https://github.com/boonaki/boonakis-tea-api)
- [ ] [view-transitions](https://docs.astro.build/en/guides/view-transitions/)
- jei man duomu baze nebutina, ar reikia ja vistiek ideti, ar galima prasisukti ir be jos
- ar galima padaryti svetainia angliskai, ar geriau lietuviskai

---

### The plan

So the core consepts are **astro** and **tailwindcss**. if you have never tuch any of these tools this shood be a good start.
The the **astro.js** fing is cool that it can work with any of auredy know tools like **vue** in my case. so one conspet is [Astro Islands](https://docs.astro.build/en/concepts/islands/) in wich you can add any frame work that you know and it wont afect oder ones, the **astro** takes care of the havy lifting

### Project Structure

    - src/* - Your project source code (components, pages, styles, etc.)
      - src/components/* - is a place thae i wood like to have all components. in diffrent folder by page, and the **global** ones in global folfer
      - src/layouts/* - is a place for the layouts that will use md files, or DB 
      - src/pages/* - is a place for contnet that works from the data inside the file
    - public/* - Your non-code, unprocessed assets (fonts, icons, etc.)
    - package.json - A project manifest.
    - astro.config.mjs - An Astro configuration file. (recommended)
    - tsconfig.json - A TypeScript configuration file. (recommended)

### Components

The reusingal things like footer and header, that will be use in difrent places. and to uncomplicate the code wall. just like funcsions in code

### Style

I beleve we shood uose the tailwind with it's class aproche to the programing, but some tings will be needed to inpement on your one in \<style\>. more [info](https://docs.astro.build/en/guides/styling/) and just take a look at [hear](https://tailwindcss.com/docs/utility-first) and a [cheet sheet](https://flowbite.com/tools/tailwind-cheat-sheet/) for the use. if you dont wnat mess wiht the tailwindcss i can just leve acomment some whate and i will make it for you

#### Tailwind

So plz just take a look at
[utility-first](https://tailwindcss.com/docs/utility-first)
[hover-focus-and-other-states](https://tailwindcss.com/docs/hover-focus-and-other-states)
~~[responsive-design](https://tailwindcss.com/docs/responsive-design)~~
[dark-mode](https://tailwindcss.com/docs/dark-mode)
[reusing-styles](https://tailwindcss.com/docs/reusing-styles)
[adding-custom-styles](https://tailwindcss.com/docs/adding-custom-styles)
[functions-and-directives](https://tailwindcss.com/docs/functions-and-directives)

### Pages

They are responsible for handling routing, data loading, and overall page layout for every page in your website. so put all the pages hear

### MarkDown

That's how we will make a lot of **post** qwickly, the idea is in a **post** folder make md files with he data that the post will need. and astro will take care of it. what why chose astro so be the main flame work. to make post qwickly. so the teas will have a tag in the top of the page with data like imige locasion name, hover text, colors, anything. the body will be the text. what will be renderd after clickng. thats the past what i cant whait for. [more](https://docs.astro.build/en/guides/markdown-content/)

### Content Collections

To make it look corect and simular we will use the. dont ywat know how to inpemented but it will me usefull. [more](https://docs.astro.build/en/guides/content-collections/)

### Internationalization

So if we want to add translasion is semi dificalt, well repetitive but posibal, so as bonus or after project we can add it. [mode](https://docs.astro.build/en/guides/internationalization/)

### Fonts

How to add fonts [more](https://docs.astro.build/en/guides/fonts/)

## Back-End

### Dependencys

- python3
- flask

Indented Code Block (expected style):

```bash
  python3 -m venv .env
  source .env/bin/activate
  pip install -r requirements.txt
```

To just run after inisiligine the flask project

```bash
  flask --app main run
```

If you whant to updata data form json you need to run
```bash
  python fileToMd.py
```
and move teas_md to Front-End/src/pages/tea/

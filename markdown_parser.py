from datetime import datetime
now = datetime.now()
f = open("agent_output.txt", "r")
text = f.read()
for i in range(1, 100):  # Assuming there won't be more than 100 pages
    text = text.replace(f'[Page {i}]', '')
slides = "##" + text.split("##")[-1]
slides = text.replace("### ", "slide-break### ").replace("###", "\n<br>\n\n###").split("slide-break")
# temp_layout = "\n---\ntransition: fade-out\n---\n\n"

theme_layout = "---\ntheme: seriph\n---\n\n"
temp_layout = "---\nlayout: bullets\n---\n\n"
intro_layout = "---\nlayout: intro\n---\n\n"
slides = slides[1:]
slides = [theme_layout, intro_layout] + slides[:1] + [temp_layout+slide for slide in slides[1:]]
f = open("slides_" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".md", "w+")
output = ''.join(slides)

f.write(output)
f.close()

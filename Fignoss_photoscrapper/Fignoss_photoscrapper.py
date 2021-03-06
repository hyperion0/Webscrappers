import bs4
import os
import urllib.request
# we have several HTML files containing all links to the pictures
# Step 1 Recuperation des noms des fichiers HTML
# Step 2 Ouverture d'un fichier
# Step 3 Exploration du fichier et recuperation de tous les liens
# div class="media_wrap"
# <img alt="img_0294" class="lowres_replace hires_approx" data-lowres-src="" width="800" height="1200"
# src="//s3.amazonaws.com/medias.photodeck.com/bafbd316-f321-42c5-abe4-64a8a7f94f18/img_0294_uxga.jpg">
# Step 5 stockage de tous les liens dans une liste
# Step 6 creation dir du nom du fichier html
# Step 7 telechargement de tous les liens dans la dir



def main():
    list_names = get_html_files_names()
    for filename in list_names:
        # output directory for images
        outdir = filename.split(".")[0]
        if not os.path.isdir(outdir):
            os.mkdir(outdir)
        alldiv = open_file(filename)
        # we can now download all images
        [dl_from_div(div, outdir) for div in alldiv]
    return

def get_html_files_names():
    # this return a list containing all files ending with "html"
    return [file for file in os.listdir('.') if file[-4:] == "html"]

def open_file(filename):
    # open the html file and return all the instances of the html element we are looking for
    with open(filename, "r", encoding='ansi') as f:
        soup = bs4.BeautifulSoup(f.read())
        alldiv = soup.find_all("img", {"height": "1200"})
    return alldiv

def dl_from_div(div,outdir):
    link = "https:"+div['src']
    image_name = div['alt']
    urllib.request.urlretrieve(link, outdir+"/"+image_name+".jpg")
    print('image downloaded')
    return
main()

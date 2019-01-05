from pydocx import PyDocX
import sys, os, time, shutil, docx

def git_push():
    os.system('git add .')
    os.system("git commit -m'backup'")
    os.system('git push')

def rename(str):
    new_str = ''
    index = 0
    for i in str:
        if str[index] == '.' and str[index + 1] == 'd' and str[index + 2] == 'o' and str[index + 3] == 'c' and str[index + 4] == 'x':
            break
        new_str  = new_str + i
        index += 1
    return new_str

def main():
    file = "../../../../Desktop/blog"
    before = dict ([(f, None) for f in os.listdir (file)])
    while True:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(file)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]

        if added:
            print("Added:", ", ".join(added))

            #get(Date)
            date = time.strftime("%m-%d-%Y %H:%M", time.localtime())
            print(date)

            #get(Header Lead Label)
            doc = docx.Document(file + "/" + " ".join(added))
            fullText = []
            header = doc.paragraphs[0].text
            label = doc.paragraphs[2].text
            lead = doc.paragraphs[4].text
            print(header)
            print(label)
            print(lead)
            type(lead)

            name = rename(" ".join(added))

            #make contents
            html = PyDocX.to_html(file + "/" + " ".join(added))
            f = open("article/" + name + ".html", 'w', encoding="utf-8")
            f.write(html)
            f.close()

            #make pages
            shutil.copy("blog-example.html","article/bolg-" + name + ".html")
            temp = open("article/bolg-" + name + ".html", "r+")
            str = '<div class="content"><object class="text" data="' + name + '.html"></object></div></body></html>'
            temp.seek(0, 2)
            temp.write(str)
            temp.close()

            #get(URL)
            url = "article/bolg-" + name + ".html"
            print(url)

            #write all elements(Date URL Header Label Lead)
            blogIndex = open("blog-index.txt",'a+')
            DUHLL = date + "###" + url + "###" + header + "###" + label + "###" + lead + "/n"
            blogIndex.write(DUHLL)
            blogIndex.close()




            after = dict([(f, None) for f in os.listdir(file)])


            #!!!!!!!
            #git_push()
        if removed:
            print("Removed:", ", ".join(removed))

        before = after


if __name__ == "__main__":
    main()
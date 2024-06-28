from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("whalefallnotes.wordpress.2024-06-28.000.xml")
collection = DOMTree.documentElement
items = collection.getElementsByTagName("item")
count = 0
for item in items:
    count = count + 1
    if item.getElementsByTagName("wp:post_type")[0].childNodes[0].data == "post":
        file_name = "{}.md".format(count)
        f = None
        f = open(
            "./training/" + file_name,
            "w",
            encoding="utf-8",
        )
        f.write("---\n")
        f.write(
            "title: %s \n" % item.getElementsByTagName("title")[0].childNodes[0].data
        )
        f.write(
            "date: %s \n"
            % item.getElementsByTagName("wp:post_date")[0].childNodes[0].data
        )
        f.write("draft: false\n")
        f.write("---\n")

        f.write("# %s\n" % item.getElementsByTagName("title")[0].childNodes[0].data)
        f.write(
            "Date: %s\n"
            % item.getElementsByTagName("wp:post_date")[0].childNodes[0].data
        )
        f.write("\n")
        if len(item.getElementsByTagName("content:encoded")[0].childNodes) > 0:
            f.write(
                item.getElementsByTagName("content:encoded")[0].childNodes[0].data
                + "\n"
            )
        f.close()

import pdfkit
import pypandoc
import os
from argparse import ArgumentParser

OUTPUT_DIR = "output/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_file_name(mk_file_path, file_list, outlist):
    print(f"【{mk_file_path}】Markdown files")
    for root, dirs, files in os.walk(mk_file_path):
        for f in files:
            each = os.path.join(root, f)
            if ".md" in each:
                file_list.append(each)
                filename = each.replace(".md", ".pdf")
                f = filename.split("\\")[-1]
                outlist.append(os.path.join(OUTPUT_DIR, f))
    print("Search Completed")
    print(f"{len(outlist)} Filed Found, {outlist}")


def convert(input, output):
    pypandoc.convert_file(input, "html", outputfile="tmp.html")
    html_head_file = open("html_head.txt", "r", encoding="utf-8")
    html_head = html_head_file.read()
    html_head_file.close()
    html_tail = "\n</body>\n</html>"
    html_body_file = open("tmp.html", "r", encoding="utf-8")
    html_body_txt = html_body_file.read()
    html_body_file.close()
    html_body = html_head + html_body_txt + html_tail
    with open("tmp.html", "w", encoding="utf-8") as f:
        f.write(html_body)
        f.close()
    pdfkit.from_file("tmp.html", output, options={"enable-local-file-access": None})
    if os.path.exists("tmp.html"):
        os.remove("tmp.html")
    print(input + " conversion successful ！")


def _init_argumentParser():
    a = ArgumentParser(usage="Markdown->PDF")
    a.add_argument("-p", "--path", required=True, type=str, help="path")
    return a.parse_args()


if __name__ == "__main__":
    args = _init_argumentParser()
    mk_file_list = []
    output_pdf_file_list = []
    failed = []
    get_file_name(args.path, mk_file_list, output_pdf_file_list)
    for i in range(len(mk_file_list)):
        try:
            convert(mk_file_list[i], output_pdf_file_list[i].replace("output", "pdfs"))
        except Exception as e:
            print(f"{mk_file_list[i]} got a problem, caused: \n{e}")
            failed.append(mk_file_list[i])
    print(f"Failed {len(failed)}, {failed}")

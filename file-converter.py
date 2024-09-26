import sys
import markdown

argument = sys.argv

if len(argument) < 4:
  print("引数が不足しています。")
else:
  if argument[1] == "markdown":
    with open(argument[2], "r") as inputfile:
      markdown_text = inputfile.read()
    html_text = markdown.markdown(markdown_text, extensions=['extra', 'sane_lists'])

    with open(argument[3], "w") as outputfile:
      outputfile.write(html_text)
  else:
    print("Markdown以外のオプションは対応外です。")
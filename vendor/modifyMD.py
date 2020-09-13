import os
import re
# 对markdown预处理包括两个步骤：
# 1.通过添加header来向jekyll指示文章样式
# 2.将.md结尾的超链接转为.html链接
header='---\nlayout: article\nsidebar:\n nav: dic\n---\n\n'
link_pattern=re.compile(r'\((.*)\.md\)')
files = os.listdir('./')

def repl(matched):
  if matched.group(1).startswith('http'):
    return matched.group(0)
  else:
    article_path=matched.group(1).split('/')[-1]
# 本地预览时链接会失效，这是因为目前使用的是绝对路径
    return '({})'.format('/fluid/'+article_path+'.html')

for fname in files:
  if (fname.endswith('.md')):
    with open(fname,'r+') as f:
      content=re.sub(link_pattern,repl,f.read())
      if not content.startswith('---'):
        content=header+content
      f.seek(0)
      f.truncate()
      f.write(content)

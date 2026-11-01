"""用 LibreOffice 打开 docx、更新目录后导出 PDF（直接 soffice --convert-to pdf 时 Word 目录是空的）。
需要系统自带的 Python 和 python3-uno（Ubuntu: apt install python3-uno）。用法：/usr/bin/python3 tools/docx2pdf.py 输入.docx 输出.pdf"""
import subprocess, sys, time, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name, p.Value = n, v; return p

src, dst = sys.argv[1], sys.argv[2]
proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore",
                         '--accept=socket,host=localhost,port=2002;urp;'])
ctx = None
for _ in range(60):
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        break
    except Exception:
        time.sleep(1)
desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), "_blank", 0, (prop("Hidden", True),))
idx = doc.getDocumentIndexes()
for i in range(idx.getCount()):
    idx.getByIndex(i).update()
doc.storeToURL(uno.systemPathToFileUrl(dst), (prop("FilterName", "writer_pdf_Export"),))
n = idx.getCount()
doc.close(True)
try:
    desktop.terminate()
except Exception:
    pass
proc.wait(timeout=30)
print("ok", n)

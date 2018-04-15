class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def output_html(self):
        path = 'D:/Python/MySampleCrawler/output.html' #输出output文件
        fout = open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

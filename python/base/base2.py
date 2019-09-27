# import xml.sax
# class XMLHandler(xml.sax.handler.ContentHandler):
#     def __init__(self):
#         self.buffer = ""
#         self.mapping = {}
#
#     def startElement(self, name, attributes):
#         # print("开始--",name,attributes.__dict__)
#         print("开始--",name,attributes._attrs)
#         # self.buffer = ""
#
#     def characters(self, data):
#         print("解析",data)
#         self.buffer += data
#
#     def endElement(self, name):
#         print("结束--",name)
#         self.mapping[name] = self.buffer
#     def getDict(self):
#         return self.mapping
# data = '''
#     <a href='123' title="12">首页</a>
# '''
#
# xh = XMLHandler()
# xml.sax.parseString(data, xh)
# ret = xh.getDict()
#
# print(ret);
# import xml.sax
# import os
# class xmlhander(xml.sax.ContentHandler):
#     def __init__(self):
#         self.id=id
#         self.stulist=[]
#         self.tag=""
#         self.studic={}
#     def startElement(self,name,attrs):
#         if name=="root":
#             self.id=attrs["id"]
#             print(self.id)
#         if name=="student":
#             self.studic["id"]=attrs["id"]
#             self.studic["score"] = attrs["score"]
#         self.tag=name
#     def characters(self,content):
#         if self.tag=="student":
#             content=content.strip()
#             if len(content)>0:
#                 # self.stulist[len(self.stulist)-1]["name"]=content
#                 self.studic["name"]=content
#         print(self.stulist)
#     def endElement(self,name):
#         if name=="student":
#             self.stulist.append(self.studic)
#             self.studic = {}
#         print(self.stulist)
# xh=xmlhander()
# path=os.path.join(os.getcwd(),"test")
# path1=os.path.join(path,"xml2.xml")
# # xml.sax.parse(path,xh)
# xml.sax.parse(path1,xh)









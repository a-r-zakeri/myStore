# from urllib.parse import parse_qs
# import uuid
# import sqlite3
# import csv
# from random import randrange
#
# def my_application(environ, start_response):
#
#     qs=parse_qs(environ['QUERY_STRING'])
#
#     if qs.__len__()==0:
#         response = """<!DOCTYPE html>
#
# <html>
#     <head>
#
#         <style>
#         div{
#
#         width:auto;
#         height:auto;
#         position:absolute;
#         left:600px;
#         top:50px;
#         }
#
#         input[type="text"]
#         {
#             font-size:40px;
#             width:40px;
#             height:50px;
#             margin:10px;
#
#         }
#
#
#
#         fieldset{
# 			width: 80%;
# 			margin: 20px auto;
# 			height:auto;
# 		}
#
# 		fieldset > fieldset {
# 			width: auto;
# 			margin: 50px auto;
# 			height:auto;
#
#
# 		}
#         td{
#         float:left;
#         }
#
#         </style>
#
#         <title>
#         Fekre Bekr!
#         </title>
#
#     </head>
#
#     <body>
#         <fieldset>
#             <legend>Fekr o Bekr!</legend>
#
#             <fieldset>
#                 <legend>Your guesses!</legend>
#
#                     <table>
#
#                     </table>
#
#                 </fieldset>
#             <button style = "width:300px; height: 50px;cursor:pointer;position:static"  onclick=SendAns()>My guess!</button>
#         </fieldset>
#         <script>
#
#
#
#
#
#
#
#
#             var WordL=0;
#             var newPlay='';
#             function color(i){
#                 if (i==0)
#                     return 'red';
#                 else if (i==1)
#                     return 'yellow';
#                 else
#                     return 'green';
#
#             };
#             function SendAns(){
#
#             var tab=document.getElementsByTagName('table')[0];
#
#             var td=document.createElement('td');
#             var br=document.createElement('br');
#             var httpRequest= new XMLHttpRequest();
#                                 httpRequest.onreadystatechange= function() {
#                                     if (httpRequest.readyState== 4) {
#                                         if(httpRequest.responseText.charAt(0)!='<'){
#                                             var retAns=JSON.parse(httpRequest.responseText);
#                                             if(WordL==0){
#                                             WordL=retAns.wordL;
#                                             newPlay=retAns.id;
#                                             }
#
#                                             else{
#
#                                                 if(retAns.status=='error'){
#                                                     alert(retAns.reason);
#
#                                                 }
#                                                 else if(retAns.won=='true'){
#                                                     alert('You won! congratulation')
#                                                 }
#                                                 else{
#
#
#                                         var inp=document.getElementsByTagName('input');
#                                         if(inp.length!=0){
#
#                                             for (i=0;i<retAns.state.length;i++){
#                                                 inp[inp.length-(retAns.state.length-i)].setAttribute('style','background-color:'+color(retAns.state[i]));
#
#                                             }
#                                         }
#
#                                         var temp='';
#
#
#
#                                         if(WordL!=0){
#
#                                             temp+='<input type="text" maxlength="1" autofocus="autofocus">';
#                                             for (i=WordL-1;i>0;i--){
#                                                 temp+='<input type="text" maxlength="1">';
#                                             }
#                                             td.innerHTML=temp;
#                                             var tr = document.createElement('tr');
#                                             tr.appendChild(td);
#                                             tab.appendChild(tr);
#                                         }
#                                         }
#                                         }
#                                     }
#                                 }
#                                 else{
#
#                                     }
#                                 };
#                                 var tempAns=document.getElementsByTagName('input');
#                                 var ans='';
#
#                                 if(tempAns.length!=0){
#
#                                     for (i=tempAns.length-WordL;i<tempAns.length;i++){
#                                         if(tempAns[i].value==''){
#                                             ans+='$';
#
#                                         }
#                                         else{ans+=tempAns[i].value;}
#                                     }
#                                 }
#
#                                 ans2='majid';
#                                 if(ans!='')
#                                     ans2=ans;
#
#                                 httpRequest.open('GET', '127.0.0.1/?id='+newPlay+'&ans='+ans2, true);
#                                 httpRequest.send();
#
#
#
#
#             }
#
#         </script>
#     </body>
#
# </html>"""
#         response_headers = [
#             ("Content-type", "text/html"),
#             ]
#
#     else:
#         if 'id' not in qs:
#             tword = word()
#             tid = uuid.uuid4()
#             dbInsert(str(tid),tword)
#             response='{"id":"'+str(tid)+'","wordL":'+str(len(tword))+'}'
#         else:
#             if getWord(qs['id'][0])[0]==0:
#                 response='{"status":"error","reason":"ID not found"}'
#             else:
#                 if check(qs['id'][0],qs['ans'][0]):
#                     response='{"status":"success","won":"true"}'
#                 else:
#                     temp=getWord(qs['id'][0])
#                     response='{"status":"success","won":"false","state":"'+checkAns(temp,qs['ans'][0])+'"}'
#
#
#
#
#         response_headers = [
#             ("Content-type", "application/json"),
#             ]
#
#     start_response("200 OK", response_headers)
#     return [bytes(response,"UTF-8"),]
#
#
# def db():
#     conn1 = sqlite3.connect('DataBase.db')
#     conn=conn1.cursor()
#     print("Opened database successfully")
#     if not conn.execute('''SELECT * FROM sqlite_master WHERE name ='Game' and type='table'; '''):
#         conn.execute('''CREATE TABLE Game
#                (ID TEXT PRIMARY KEY     NOT NULL,
#                WORD           TEXT    NOT NULL);
#                ''')
#         conn1.commit()
#         conn.close()
#
# def dbInsert(id,word1):
#     conn1 = sqlite3.connect('DataBase.db')
#     conn=conn1.cursor()
#     conn.execute("INSERT INTO Game (ID,WORD)  VALUES (?,?)", (id,word1))
#     conn1.commit()
#
#     conn.close()
#
# def getWord(id1):
#     conn1 = sqlite3.connect('DataBase.db')
#     conn=conn1.cursor()
#     conn.execute('SELECT WORD from Game where ID="'+id1+'"')
#     row = conn.fetchone()
#     if row is not None:
#         conn.close()
#         return 1, row[0]
#     else:
#         conn.close()
#         return 0, ''
#
#     conn.close()
#
# def check(id,ans):
#     if(getWord(id)[1]==ans):
#         return True
#     else:
#         return False
#
#
# def word():
#     inputFile = open('words.csv', 'r')
#     reader = csv.reader(inputFile)
#     irand = randrange(0,2818)
#     ans=''
#     for i ,w in enumerate(reader):
#         if i==irand:
#             return w[0]
#     return 'majidWord'
#
# def checkAns(w,a):
#     if a=='majid':
#         return ''
#     ans=''
#     for i in range(0,len(w[1])):
#
#         if w[1][i]==a[i]:
#             ans+='2'
#         else:
#             bool=True
#             for j in range(0,len(w[1])):
#                 if w[1][j]==a[i]:
#                     bool=False
#                     ans+='1'
#                     break
#             if bool:
#                 ans+='0'
#     return ans
#
#
#
#
#
#
# if __name__ == "__main__":
#     from wsgiref.simple_server import make_server
#     httpd = make_server('localhost', 8000, my_application)
#     httpd.serve_forever()

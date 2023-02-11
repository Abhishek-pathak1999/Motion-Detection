from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Chat
import cv2
import numpy as np
import threading


cap = cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2(300,400, False)
while(True):
    success, frame = cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow("fgbg", fgmask)

    count=np.count_nonzero(fgmask)
    if count>5000:
        print("xyz")

    key=cv2.waitKey(1) & 0xff
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
class VideoChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive_json(self, content):
        if(content['command'] == 'join_room'):   
            await self.channel_layer.group_add(content['room'],self.channel_name)
            print(1)
            
        elif(content['command'] == 'join'):
            await self.channel_layer.group_send(content['room'],{
                'type':'join.message',
            })
            print('join')
            
        elif(content['command'] == 'offer'):
            await self.channel_layer.group_send(content['room'],{
                'type':'offer.message',
                'offer':content['offer']
            })
            print('offer')
        elif(content['command'] == 'answer'):
            await self.channel_layer.group_send(content['room'],{
                'type':'answer.message',
                'answer':content['answer']
            })
            print('answer')
        elif(content['command'] == 'candidate'):
            await self.channel_layer.group_send(content['room'],{
                'type':'candidate.message',
                'candidate':content['candidate'],
                'iscreated':content['iscreated']
            })
            print('candidate')
    async def join_message(self,event):
        await self.send_json({
            'command':'join',
        })
        
    
    async def offer_message(self,event):
        await self.send_json({
            'command':'offer',
            'offer':event['offer']
        })
        
    
    async def answer_message(self,event):
        await self.send_json({
            'command':'answer',
            'answer':event['answer']
        })
    
    async def candidate_message(self,event):
        await self.send_json({
            'command':'candidate',
            'candidate':event['candidate'],
            'iscreated':event['iscreated']
        })
        
# serverless na server illa na aartham illa we can't managed
'''
computing server - from the start os, volume, network,storage external storage ,internal storage,auto scalling  we manage
lamba serverless  - when u come lamba we can't manage because its serverless (aws managed)simpley code only run

'''

#kutchi naiye maintain server he---to ws managed server aagayaa

#Trigger------Eppo run aaganum (S3, API, schedule…)



# developer friendly only developer handle
# daily pay panna theva illa yappala code computing(run) aaguthu appo pannum pay
# like ni8 time less use lesspay ... weekend no use 0 pay


'''
Lamba trigger theory
        🎬 Raw Movie Upload
                |
                v
        ┌─────────────────┐
        |       S3        |
        |  (raw-movies)   |
        └─────────────────┘
                |
        (S3 Event Trigger)
                |
                v
        ┌─────────────────┐
        |     Lambda      |
        |  (Job starter)  |
        └─────────────────┘
                |
                v
   ┌───────────────────────────┐
   |  Video Processor Service  |
   | (MediaConvert / ECS/EC2)  |
   └───────────────────────────┘
                |
      Convert into multiple qualities
                |
                v
        ┌──────────────────────────────┐
        |             S3              |
        |   (processed videos/chunks) |
        └──────────────────────────────┘
                |
                v
        🌍 CDN (CloudFront)
                |
                v
      📱 Mobile / 💻 Laptop / 📺 TV
      (720p / 1080p / 4K auto select)

'''


# how to create lamba funcation and how to traggier


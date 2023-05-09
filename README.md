## Semantic search engine for the internet !
<img src="./assets/architecture.png"></img>

### ToDo
[ ] where to get the dataset ? (youtube maybe ?)<br>
[ ] process the dataset and create some kind of JSON file (refr - mail)

### Research (More like documenting my work flow)
So this is just my initital thinking BUT can I find .vrts or .vtt files ? I don't think so !<br>
What if I could create .vrts or .vtt (I prefer .vtt more its easy and fun) this could expand the operations ! <br>
Now how do I create my own .vtt file ? Okay so how the .vtt file looks like - <br>
1. it contains basic things such as the time and the dialogue spoken in that time frame !<br>
<a href="./smpleDataset/">.vtt sampe file </a>
<br>
Can I use whisper ? <br>
https://cdn.openai.com/papers/whisper.pdf <br>
I think I will go with Whisper and convert some video data into audio transcription and convert all of it to a .vtt file and then continue with the rest of the architecture ! <br>
This approch drastically improves the scope of the project, now the project is not limited to a ceratin dataset or some bullshit <br>
NOW the question is what video dataset I should choose ? I want a dataset that should unlock full potential of my search engine <br>
1. Mark Rober (this is the first thing what comes to my mind when I think enducational and a lot of real world fotage ) Yeah I will go with MARK ROBER ! <br>

With this I have a .vtt file with dialogues and the time frame where the dialogue is being spoken ! <br>
The next step is to extract out relevent frames from the time buffer where the dialogue is being spoken with FFMPEG<br><br>

And extract out relevent information from those frames through CoCa and concatenate it with the dialogues into a JSON <br>

Creating Embeddings <br><br>

use the metadata, videoID, timestamp, dialogues, and the embeddings per sentence and store it into a vector database <br>
for embedding use some MiniLM model (abacaj on twitter). And for storing it use Weaviate <br><br>

Frontend - Backend <br>

use ChatGPT to create a JS based frontend (using Vue and Vite) and use FASTAPI which would provide a RESTful interface <br>

Frontend must include search filtering and sorting <br>

write unit tests with PyTest <br>







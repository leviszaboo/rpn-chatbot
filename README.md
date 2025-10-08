# RDM Chatbot

Real‑time AI assistant built with a Flask backend and a React frontend, designed to help VU Amsterdam researchers and students quickly find information from the VU Research Data Management Handbook. It uses the Nebula DeepSeek‑R1 8B reasoning model via the Nebula API and streams responses to the frontend using Server‑Sent Events for a dynamic experience

### How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/leviszaboo/rdm-chatbot.git
   cd rdm-chatbot
   ```
2. **Add your Nebula API key**
   ```bash
   echo "NEBULA_API_KEY=your_api_key_here" > backend/.env
   ```
3. **Start with docker-compose**
   ```bash
   docker-compose up -d
   ```
4. **Open in your browser**
   
   Visit [http://localhost](http://localhost) after configuration.

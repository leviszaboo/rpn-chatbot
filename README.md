# RDM Chatbot

Real‑time AI assistant built with a Flask backend and a React frontend, designed to help VU Amsterdam researchers and students quickly find information from the VU Research Data Management Handbook. It uses the Nebula DeepSeek‑R1 8B reasoning model via the Nebula API and streams responses to the frontend using Server‑Sent Events for a dynamic experience.

<img width="1018" height="679" alt="Screenshot 2025-10-08 at 18 12 44" src="https://github.com/user-attachments/assets/e23c0813-eb7c-4064-ac5c-7dbe31ef5993" />

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

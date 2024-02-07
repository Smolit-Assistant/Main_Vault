// communicationModule.js
export class CommunicationModule {
    constructor(outputCallback) {
        this.outputCallback = outputCallback;
    }

    async sendChatMessage(message) {
        this.outputCallback('Sending...', true);
        try {
            const response = await fetch('https://api.dev-gpt.com/chat', {
                method: 'POST',
                body: JSON.stringify({ message }),
                headers: { 'Content-Type': 'application/json' }
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            this.outputCallback(data.reply);
        } catch (error) {
            this.outputCallback(`Fehler: ${error.message}`);
        }
    }
}

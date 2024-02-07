// userSettingsModule.js
export class UserSettingsModule {
    constructor(pluginInstance) {
        this.plugin = pluginInstance;
        this.settings = this.loadSettings();
    }

    loadSettings() {
        // Laden der Einstellungen aus dem lokalen Speicher
        return JSON.parse(localStorage.getItem('pluginGeneratorSettings')) || {};
    }

    saveSettings() {
        // Speichern der Einstellungen im lokalen Speicher
        localStorage.setItem('pluginGeneratorSettings', JSON.stringify(this.settings));
    }

    saveChatHistory(chatHistory) {
        this.settings.chatHistory = chatHistory;
        this.saveSettings();
    }

    loadChatHistory() {
        return this.settings.chatHistory || [];
    }
}

// errorHandlingModule.js
export class ErrorHandlingModule {
    constructor(pluginInstance) {
        this.plugin = pluginInstance;
    }

    displayErrorMessage(error) {
        // Anzeige einer benutzerfreundlichen Fehlermeldung
        const errorMessage = `Ein Fehler ist aufgetreten: ${error.message}`;
        this.plugin.displayChatMessage(errorMessage);
    }

    provideUserGuidance() {
        // Bereitstellung von Hilfestellungen für den Benutzer
        const guidanceMessage = "Tippe 'Hilfe' für eine Anleitung zur Nutzung des Plugins.";
        this.plugin.displayChatMessage(guidanceMessage);
    }
}

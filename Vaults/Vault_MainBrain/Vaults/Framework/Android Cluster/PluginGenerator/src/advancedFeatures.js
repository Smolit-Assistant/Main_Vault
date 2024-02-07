// advancedFeatures.js
export class AdvancedFeatures {
    constructor(pluginInstance) {
        this.plugin = pluginInstance;
    }

    addInteractiveElements() {
        // Hinzufügen eines Dropdown-Menüs zur Auswahl des Plugin-Typs
        const templateSelector = this.plugin.createEl('select', { cls: 'template-selector' });
        templateSelector.createEl('option', { value: 'notiz', text: 'Notiz-Plugin' });
        templateSelector.createEl('option', { value: 'standard', text: 'Standard-Plugin' });
        this.plugin.containerEl.appendChild(templateSelector);

        // Hinzufügen eines Buttons zur Generierung des Codes
        const generateButton = this.plugin.createEl('button', { text: 'Generiere Code', cls: 'generate-button' });
        generateButton.addEventListener('click', () => {
            const selectedTemplate = templateSelector.value;
            this.generateCodeBasedOnTemplate(selectedTemplate);
        });
        this.plugin.containerEl.appendChild(generateButton);
    }

    generateCodeBasedOnTemplate(templateType) {
        let generatedCode;
        switch (templateType) {
            case 'notiz':
                generatedCode = this.plugin.pluginGeneratorModule.generateNoteFunctionPlugin();
                break;
            case 'standard':
            default:
                generatedCode = this.plugin.pluginGeneratorModule.generateDefaultPlugin();
                break;
        }
        this.plugin.displayChatMessage(`Generierter Code: \n${generatedCode}`);
    }
}

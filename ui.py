import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt

class DragDropWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Impostazioni finestra
        self.setWindowTitle("Drag and Drop - Carica Excel")
        self.setGeometry(100, 100, 800, 600)

        # Layout
        self.layout = QVBoxLayout()

        # Etichetta per il drag-and-drop
        self.label = QLabel("Trascina un file Excel qui", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Tabella per visualizzare i dati del file Excel
        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

        # Pulsante per caricare il file tramite finestra di dialogo
        self.load_button = QPushButton("Carica File Excel", self)
        self.load_button.clicked.connect(self.load_file_dialog)
        self.layout.addWidget(self.load_button)

        # Imposta la finestra per supportare il drag-and-drop
        self.setAcceptDrops(True)

        # Aggiungi il layout alla finestra
        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Ottieni il file path dal drag-and-drop
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.label.setText(f"File caricato: {file_path}")
        self.read_excel(file_path)

    def load_file_dialog(self):
        # Apri la finestra di dialogo per selezionare un file Excel
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleziona File Excel", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            self.label.setText(f"File caricato: {file_path}")
            self.read_excel(file_path)

    def read_excel(self, file_path):
        try:
            # Leggi il file Excel usando pandas
            if file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path, engine="openpyxl")
            elif file_path.endswith(".xls"):
                df = pd.read_excel(file_path, engine="xlrd")
            else:
                raise ValueError("Formato non supportato. Usa .xls o .xlsx")
            
            # Mostra il contenuto del file nella tabella
            self.display_table(df)

        except Exception as e:
            self.label.setText(f"Errore nel caricare il file: {str(e)}")

    def display_table(self, df):
        # Imposta il numero di righe e colonne della tabella
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        # Aggiungi i dati al widget della tabella
        for row in range(len(df)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table.setItem(row, col, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.show()
    sys.exit(app.exec_())


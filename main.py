import streamlit as st
import fitz  # PyMuPDF
import io

def modify_pdf_text(file, old_new_text_pairs):
    # Ouvrir le document PDF à partir du fichier téléchargé
    document = fitz.open(stream=file.read(), filetype="pdf")

    for page_num in range(len(document)):
        page = document[page_num]
        
        for old_text, new_text in old_new_text_pairs:
            text_instances = page.search_for(old_text)

            for inst in text_instances:
                # Extraire les informations de texte
                text_page = page.get_text("dict")
                for block in text_page["blocks"]:
                    if "lines" in block:  # Vérifier si le bloc contient des lignes (contenu texte)
                        for line in block["lines"]:
                            for span in line["spans"]:
                                if old_text in span["text"]:
                                    # Récupérer la taille de la police de l'ancien texte
                                    font_size = span["size"]

                                    # Effacer le texte existant en ajoutant un rectangle blanc par-dessus
                                    page.add_redact_annot(inst)
                                    page.apply_redactions()

                                    # Ajouter le nouveau texte au même endroit avec la même taille de police
                                    tl_x, tl_y = inst.tl  # Coin supérieur gauche de l'instance trouvée
                                    page.insert_text((tl_x, tl_y + 12), new_text, fontsize=font_size, fontname="helv", color=(0, 0, 0))

    # Enregistrer le PDF modifié dans un buffer
    output_pdf = io.BytesIO()
    document.save(output_pdf)
    document.close()
    
    # Revenir au début du buffer
    output_pdf.seek(0)
    return output_pdf

# Interface Streamlit
st.title("Modifier le texte d'un PDF")

# Télécharger le fichier PDF
uploaded_file = st.file_uploader("Téléchargez votre PDF", type="pdf")

# Ajouter des paires de texte à modifier
old_new_text_pairs = []
num_pairs = st.number_input("Combien de paires de texte souhaitez-vous changer ?", min_value=1, max_value=10, value=1)

for i in range(num_pairs):
    old_text = st.text_input(f"Texte à remplacer (ancien) {i+1}", key=f"old_text_{i}")
    new_text = st.text_input(f"Nouveau texte {i+1}", key=f"new_text_{i}")
    if old_text and new_text:
        old_new_text_pairs.append((old_text, new_text))

# Bouton pour lancer la modification
if st.button("Modifier le PDF") and uploaded_file is not None:
    # Modifier le texte du PDF
    output_pdf = modify_pdf_text(uploaded_file, old_new_text_pairs)

    # Télécharger le fichier PDF modifié
    st.download_button(label="Télécharger le PDF modifié", data=output_pdf, file_name=str(uploaded_file.name)+"modified.pdf", mime="application/pdf")

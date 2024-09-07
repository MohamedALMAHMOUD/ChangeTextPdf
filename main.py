import streamlit as st
import fitz  # PyMuPDF
import io

# Définir la taille maximale du fichier (en octets) : 10 Mo
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 Mo

# Fonction pour modifier plusieurs textes dans le PDF
def modify_multiple_texts(pdf_file, text_replacements):
    # Ouvrir le fichier PDF depuis les bytes
    document = fitz.open(stream=pdf_file, filetype="pdf")
    output_pdf = io.BytesIO()  # Créer un buffer pour le fichier PDF modifié
    
    # Parcourir les pages du document
    for page_num in range(len(document)):
        page = document[page_num]
        
        for old_text, new_text in text_replacements:
            text_instances = page.search_for(old_text)
            
            # Remplacer les occurrences du texte trouvé
            for inst in text_instances:
                # Effacer le texte existant en ajoutant un rectangle blanc par-dessus
                page.add_redact_annot(inst)
                page.apply_redactions()

                # Ajouter le nouveau texte au même endroit
                tl_x, tl_y = inst.tl  # Coin supérieur gauche de l'instance trouvée
                page.insert_text((tl_x, tl_y+12), new_text, fontsize=12, color=(0, 0, 0))

    # Sauvegarder le fichier modifié dans le buffer
    document.save(output_pdf)
    document.close()
    
    output_pdf.seek(0)  # Revenir au début du fichier pour la lecture
    return output_pdf

# Interface Streamlit pour uploader un fichier PDF
st.title("Téléchargez un fichier PDF et remplacez plusieurs textes")

uploaded_file = st.file_uploader("Choisissez un fichier PDF", type=["pdf"])

# Ajouter un champ pour le nombre de textes à remplacer
num_replacements = st.number_input("Combien de textes souhaitez-vous remplacer ?", min_value=1, max_value=10, value=1)

# Créer des champs dynamiques pour l'entrée des textes à remplacer
text_replacements = []
for i in range(num_replacements):
    old_text = st.text_input(f"Texte à remplacer #{i+1}")
    new_text = st.text_input(f"Nouveau texte #{i+1}")
    if old_text and new_text:
        text_replacements.append((old_text, new_text))

if uploaded_file is not None:
    # Récupérer la taille du fichier
    file_size = uploaded_file.size
    
    # Vérifier si la taille du fichier dépasse la limite
    if file_size > MAX_FILE_SIZE:
        st.error(f"Le fichier dépasse la taille maximale autorisée de 10 Mo. "
                 f"Taille actuelle: {file_size / (1024 * 1024):.2f} Mo")
    else:
        # Si la taille du fichier est acceptable, traiter le fichier
        st.success(f"Fichier {uploaded_file.name} téléchargé avec succès!")
        st.write(f"Taille du fichier : {file_size / (1024 * 1024):.2f} Mo")
        
        if text_replacements:
            # Modifier les textes dans le fichier PDF
            modified_pdf = modify_multiple_texts(uploaded_file.read(), text_replacements)

            # Proposer le fichier modifié à télécharger
            st.download_button(
                label="Télécharger le PDF modifié",
                data=modified_pdf,
                file_name=f"modified_{uploaded_file.name}",
                mime="application/pdf"
            )
        else:
            st.warning("Veuillez entrer au moins une paire de texte à remplacer et un nouveau texte.")
else:
    st.write("Veuillez télécharger un fichier PDF.")

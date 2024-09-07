{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Retrieving notices: ...working... done\n",
      "\n",
      "CondaValueError: no package names supplied\n",
      "# Example: conda update -n myenv scipy\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import fitz  # PyMuPDF\n",
    "import io\n",
    "\n",
    "def modify_pdf_text(file, old_new_text_pairs):\n",
    "    # Ouvrir le document PDF à partir du fichier téléchargé\n",
    "    document = fitz.open(stream=file.read(), filetype=\"pdf\")\n",
    "\n",
    "    for page_num in range(len(document)):\n",
    "        page = document[page_num]\n",
    "        \n",
    "        for old_text, new_text in old_new_text_pairs:\n",
    "            text_instances = page.search_for(old_text)\n",
    "\n",
    "            for inst in text_instances:\n",
    "                # Extraire les informations de texte\n",
    "                text_page = page.get_text(\"dict\")\n",
    "                for block in text_page[\"blocks\"]:\n",
    "                    if \"lines\" in block:  # Vérifier si le bloc contient des lignes (contenu texte)\n",
    "                        for line in block[\"lines\"]:\n",
    "                            for span in line[\"spans\"]:\n",
    "                                if old_text in span[\"text\"]:\n",
    "                                    # Récupérer la taille de la police de l'ancien texte\n",
    "                                    font_size = span[\"size\"]\n",
    "\n",
    "                                    # Effacer le texte existant en ajoutant un rectangle blanc par-dessus\n",
    "                                    page.add_redact_annot(inst)\n",
    "                                    page.apply_redactions()\n",
    "\n",
    "                                    # Ajouter le nouveau texte au même endroit avec la même taille de police\n",
    "                                    tl_x, tl_y = inst.tl  # Coin supérieur gauche de l'instance trouvée\n",
    "                                    page.insert_text((tl_x, tl_y + 8), new_text, fontsize=font_size, fontname=\"helv\", color=(0, 0, 0))\n",
    "\n",
    "    # Enregistrer le PDF modifié dans un buffer\n",
    "    output_pdf = io.BytesIO()\n",
    "    document.save(output_pdf)\n",
    "    document.close()\n",
    "    \n",
    "    # Revenir au début du buffer\n",
    "    output_pdf.seek(0)\n",
    "    return output_pdf\n",
    "\n",
    "# Interface Streamlit\n",
    "st.title(\"Modifier le texte d'un PDF\")\n",
    "\n",
    "# Télécharger le fichier PDF\n",
    "uploaded_file = st.file_uploader(\"Téléchargez votre PDF\", type=\"pdf\")\n",
    "\n",
    "# Ajouter des paires de texte à modifier\n",
    "old_new_text_pairs = []\n",
    "num_pairs = st.number_input(\"Combien de paires de texte souhaitez-vous changer ?\", min_value=1, max_value=10, value=1)\n",
    "\n",
    "for i in range(num_pairs):\n",
    "    old_text = st.text_input(f\"Texte à remplacer (ancien) {i+1}\", key=f\"old_text_{i}\")\n",
    "    new_text = st.text_input(f\"Nouveau texte {i+1}\", key=f\"new_text_{i}\")\n",
    "    if old_text and new_text:\n",
    "        old_new_text_pairs.append((old_text, new_text))\n",
    "\n",
    "# Bouton pour lancer la modification\n",
    "if st.button(\"Modifier le PDF\") and uploaded_file is not None:\n",
    "    # Modifier le texte du PDF\n",
    "    output_pdf = modify_pdf_text(uploaded_file, old_new_text_pairs)\n",
    "\n",
    "    # Télécharger le fichier PDF modifié\n",
    "    st.download_button(label=\"Télécharger le PDF modifié\", data=output_pdf, file_name=\"modified_pdf.pdf\", mime=\"application/pdf\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

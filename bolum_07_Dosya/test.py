{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "ogrenciler = [\"Engin\", \"Derin\", \"Salih\", \"Ali\",\"Ömer\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"test.txt\", \"w\" ,encoding = 'utf-8') as f:\n",
    "    for line in ogrenciler:\n",
    "        f.write((line+\"\\n\"))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "liste = []\n",
    "with open(\"c02_Listeyi_dosyaya_yazma.ipynb\", \"r+\" ,encoding = 'utf-8') as f:\n",
    "    for line in f:\n",
    "        liste.append(line)"
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
   "display_name": "Python 3.10.5 64-bit",
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
   "version": "3.10.5"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b885c526da3326e581d3a88563282ab625602807b12d7b4af8a2a7f32a015837"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

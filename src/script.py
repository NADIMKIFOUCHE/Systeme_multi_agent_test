import psycopg2
from sentence_transformers import SentenceTransformer
import re

# 🔌 connexion DB
conn = psycopg2.connect(
    dbname="ragdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# 🧠 modèle embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# 📄 lire le fichier
with open("cv.txt", "r", encoding="utf-8") as f:
    data = f.read()

# ✂️ split sur chaque CV
cvs = re.split(r"=== CV \d+ ===", data)

# enlever les vides
cvs = [cv.strip() for cv in cvs if cv.strip()]

print(f"{len(cvs)} CV détectés")

# 🔁 boucle insertion
for i, cv in enumerate(cvs):
    
    # 🧠 embedding
    embedding = model.encode(cv).tolist()
    
    # 🗂️ source simple
    source = f"cv_{i+1}"

    # 📥 insertion
    cursor.execute(
        "INSERT INTO documents (content, embedding, source) VALUES (%s, %s, %s)",
        (cv, embedding, source)
    )

    print(f"CV {i+1} inséré")

# 💾 commit
conn.commit()

# 🔒 fermeture
cursor.close()
conn.close()

print("✅ Tous les CV ont été insérés")
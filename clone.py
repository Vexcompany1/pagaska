import os
import shutil

def clone_sessions(source_account, new_accounts):
    source_path = f"sessions/{source_account}"
    
    if not os.path.exists(source_path):
        print("Sumber sesi tidak ditemukan!")
        return
    
    for account in new_accounts:
        new_path = f"sessions/{account}"
        shutil.copytree(source_path, new_path)
        print(f"Berhasil meng-clone sesi untuk {account}")

# Contoh penggunaan
clone_sessions("akun1", ["akun3", "akun4"])

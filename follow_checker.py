from config import Bot

def main():
	print("Menjalankan pengecekan akun yang mengikuti...")

def check_follow_status(account):
    """
    Mengecek daftar pengikut dari akun target.
    Mengembalikan daftar followers atau pesan error jika gagal.
    """
    try:
        if bot is None:
            raise ValueError("Bot belum diinisialisasi dengan benar")
        
        if not hasattr(bot, "get_user_followers"):
            raise AttributeError("Bot tidak memiliki metode 'get_user_followers'")

        # Panggil fungsi untuk mendapatkan daftar pengikut
        followers = bot.get_user_followers(account)
        return followers

    except Exception as e:
        return f"Terjadi kesalahan: {e}"
	    

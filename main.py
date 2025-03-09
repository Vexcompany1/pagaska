import follow_checker
import like_posts

def main():
    print("Memeriksa akun yang sudah diterima...")
    follow_checker.main()
    
    print("Memulai proses like...")
    like_posts.main()

if __name__ == "__main__":
    main()
    
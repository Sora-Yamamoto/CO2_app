import time

import matplotlib.pyplot as plt


def save_pw_image(df):
    if df.is_empty():
        print("The DataFrame is empty. No image was saved.")
        return
    # time
    formatted_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    date_folder_name = time.strftime("%Y%m%d", time.localtime())
    # Intensity data
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("I_435nm"), marker="o", label="I_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("I_490nm"), marker="o", label="I_490nm", color="green")
    plt.plot(df.select("Time"), df.select("I_590nm"), marker="o", label="I_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("I_735nm"), marker="o", label="I_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Intensity")
    plt.title("Intensity Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/pw_intensity/{formatted_time}_I_pw.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_I_pw.png")
    # Reference data visualization
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("Ref_Dark"), marker="o", label="Ref_Dark", color="black")
    plt.plot(df.select("Time"), df.select("Ref_435nm"), marker="o", label="Ref_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("Ref_490nm"), marker="o", label="Ref_490nm", color="green")
    plt.plot(df.select("Time"), df.select("Ref_590nm"), marker="o", label="Ref_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("Ref_735nm"), marker="o", label="Ref_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Reference Intensity")
    plt.title("Reference Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/pw_reference/{formatted_time}_ref_pw.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_ref_pw.png")
    # Signal data visualization
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("Sig_Dark"), marker="o", label="Sig_Dark", color="black")
    plt.plot(df.select("Time"), df.select("Sig_435nm"), marker="o", label="Sig_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("Sig_490nm"), marker="o", label="Sig_490nm", color="green")
    plt.plot(df.select("Time"), df.select("Sig_590nm"), marker="o", label="Sig_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("Sig_735nm"), marker="o", label="Sig_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Signal Intensity")
    plt.title("Signal Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/pw_signal/{formatted_time}_sig_pw.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_sig_pw.png")


def save_co2_image(df, ppm):
    if df.is_empty():
        print("The DataFrame is empty. No image was saved.")
        return
    
    # 現在時刻のフォーマット
    formatted_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    date_folder_name = time.strftime("%Y%m%d", time.localtime())

    # ★ pCO₂ の時間変化グラフを追加 ★
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("pCO2"), marker="o", label="pCO₂", color="purple")
    plt.xlabel("Time[s]")
    plt.ylabel("pCO₂ (ppm)")
    plt.title("pCO₂ Data Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/co2_pco2/{formatted_time}_{ppm}_pCO2_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_pCO2_co2.png")

    # A_R の時間変化
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("A_R"), marker="o")
    plt.xlabel("Time[s]")
    plt.ylabel("A_R")
    plt.title("A_R data")
    plt.grid(True)
    plt.savefig(f"data/type/co2_A_R/{formatted_time}_{ppm}_A_R_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_A_R_co2.png")

    # 吸光度データ
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("A_435nm"), marker="o", label="A_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("A_490nm"), marker="o", label="A_490nm", color="green")
    plt.plot(df.select("Time"), df.select("A_590nm"), marker="o", label="A_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("A_735nm"), marker="o", label="A_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Absorbance")
    plt.title("Absorbance Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/co2_abs/{formatted_time}_{ppm}_A_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_A_co2.png")

    # 強度データ
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("I_435nm"), marker="o", label="I_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("I_490nm"), marker="o", label="I_490nm", color="green")
    plt.plot(df.select("Time"), df.select("I_590nm"), marker="o", label="I_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("I_735nm"), marker="o", label="I_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Intensity")
    plt.title("Intensity Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/co2_intensity/{formatted_time}_{ppm}_I_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_I_co2.png")

    # 参照データ
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("Ref_Dark"), marker="o", label="Ref_Dark", color="black")
    plt.plot(df.select("Time"), df.select("Ref_435nm"), marker="o", label="Ref_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("Ref_490nm"), marker="o", label="Ref_490nm", color="green")
    plt.plot(df.select("Time"), df.select("Ref_590nm"), marker="o", label="Ref_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("Ref_735nm"), marker="o", label="Ref_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Reference Intensity")
    plt.title("Reference Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/co2_reference/{formatted_time}_{ppm}_ref_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_ref_co2.png")

    # シグナルデータ
    plt.figure(figsize=(10, 5))
    plt.plot(df.select("Time"), df.select("Sig_Dark"), marker="o", label="Sig_Dark", color="black")
    plt.plot(df.select("Time"), df.select("Sig_435nm"), marker="o", label="Sig_435nm", color="blue")
    plt.plot(df.select("Time"), df.select("Sig_490nm"), marker="o", label="Sig_490nm", color="green")
    plt.plot(df.select("Time"), df.select("Sig_590nm"), marker="o", label="Sig_590nm", color="orange")
    plt.plot(df.select("Time"), df.select("Sig_735nm"), marker="o", label="Sig_735nm", color="red")
    plt.xlabel("Time[s]")
    plt.ylabel("Signal Intensity")
    plt.title("Signal Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/type/co2_signal/{formatted_time}_{ppm}_sig_co2.png")
    plt.savefig(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_sig_co2.png")


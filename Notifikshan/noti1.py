from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    "Error Aa gya jyyy",
    "Payn, Ma keha wada kam pe gya jy ",
    duration=20,
    icon_path="icon.ico",
    threaded=True
)

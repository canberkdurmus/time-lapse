from time_lapse import TimeLapse

if __name__ == '__main__':
    tl = TimeLapse(1, max_frames=240, resolution=(1280, 720), fps=24, data_folder='image')
    tl.thread.start()
    tl.thread.join()

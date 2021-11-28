from time_lapse import TimeLapse

if __name__ == '__main__':
    tl = TimeLapse(1, max_frames=3600)
    tl.thread.start()
    tl.thread.join()

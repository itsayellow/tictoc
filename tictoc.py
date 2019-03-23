import time
import datetime

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def start(self):
        self.start_time = time.time()

    def eltime(self):
        return time.time() - self.start_time

    def eltime_pr(self, outstring, **print_args):
        eltime = time.time() - self.start_time
        elapsed = str(datetime.timedelta(seconds=eltime))
        print(outstring + elapsed, **print_args)

    def progress_pr(self, frac_done=0.0, **print_args):
        el_time = time.time() - self.start_time
        togo_time = el_time * (1/frac_done - 1)

        elapsed_str = str(datetime.timedelta(seconds=int(el_time)))
        togo_str = str(datetime.timedelta(seconds=int(togo_time)))
        perc_str = "%2.f"%(frac_done*100)

        elapsed_str = "Elapsed: " + elapsed_str
        togo_str = "Est. Remaining: " + togo_str
        perc_str = perc_str + "% Complete"

        # make sure to erase end of string at least
        print("\r%s%36s%29s"%(perc_str,togo_str,elapsed_str),
                end="", **print_args)

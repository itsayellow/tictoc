import time
import datetime

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def start(self):
        """Start this timer.
        """
        self.start_time = time.time()

    def eltime(self):
        """Return number of seconds since start()

        Returns:
            float: number of seconds since this instance's start() was called.
        """
        return time.time() - self.start_time

    def eltime_h(self):
        """Return number of seconds since start()

        Returns:
            str: human-readable time since this instance's start() was called.
        """
        eltime = time.time() - self.start_time
        return str(datetime.timedelta(seconds=eltime))

    def eltime_pr(self, outstring, **print_args):
        print(outstring + self.eltime_h(), **print_args)

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

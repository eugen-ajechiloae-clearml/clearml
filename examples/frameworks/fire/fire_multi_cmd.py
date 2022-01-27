from clearml import Task
import fire


def hello(count, name="clearml", prefix="prefix_", suffix="_suffix", **kwargs):
    for _ in range(count):
        print("Hello %s%s%s!" % (prefix, name, suffix))


def serve(addr, port, should_serve=False):
    Task.init(project_name="examples", task_name="fire multi command")
    if not should_serve:
        print("Not serving")
    else:
        print("Serving on %s:%s" % (addr, port))


if __name__ == "__main__":
    Task.init(project_name="examples", task_name="fire multi command")
    fire.Fire()

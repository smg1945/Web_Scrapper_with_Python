from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


# AttributeError: 'int' object has no attribute 'find'
# indeed_jobs = get_indeed_jobs()


so_jobs = get_so_jobs()
jobs = so_jobs
save_to_file(jobs)
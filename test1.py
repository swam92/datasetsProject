import redis, redisbayes
rb = redisbayes.RedisBayes(redis=redis.Redis())

rb.train('good', 'sunshine drugs love sex lobster sloth')
rb.train('bad', 'fear death horror government zombie god')

assert rb.classify('sloths are so cute i love them') == 'good'
assert rb.classify('i fear god and love the government') == 'bad'

print rb.score('i fear god and love the government')

rb.untrain('good', 'sunshine drugs love sex lobster sloth')
rb.untrain('bad', 'fear death horror government zombie god')
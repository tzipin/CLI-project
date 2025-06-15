class CommitDetails:
    def __init__(self, index, date, message):
        self.hash_code = str(index) + "_" + str(date.strftime("%Y-%m-%d"))
        self.date = date
        self.message = message

    def __repr__(self):
        return '{"hash_code": "%s",  "date": "%s",  "message": "%s" }' % (self.hash_code, self.date, self.message)

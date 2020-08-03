class InferenceRule:
    def getqueries(self):
        return []
    def maketriples(self, binding):
        return self._maketriples(**binding)

class WestCoastRule(InferenceRule):
    def getqueries(self):
        sfoquery = [('?company', 'headquarters', 'San_Francisco_California')]
        seaquery = [('?company', 'headquarters', 'Seattle_Washington')]
        laxquery = [('?company', 'headquarters', 'Los_Angelese_California')]
        porquery = [('?company', 'headquarters', 'Portland_Oregon')]

        return [sfoquery, seaquery, laxquery, porquery]
    def _maktriples(self, company):
        return [(company, 'on_coast', 'west_coast')]
# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: HealthTrack
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['name', 'note']
        
        results = []
        for item in self.data:
            match_found = False
            for field_name in fields:
                value = item.get(field_name)
                if value and str(value).lower().find(query.lower()) != -1:
                    match_found = True
                    break
            
            if match_found:
                results.append(item)
        
        return results

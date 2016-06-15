import geoalchemy2

class Geometry(geoalchemy2.Geometry):

    def column_expression(self, col):
        return geoalchemy2.types.func.ST_AsText(col, type_=self)

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is not None:
                return WKTElement(value, srid=self.srid)
        return process


class WKTElement(geoalchemy2.WKTElement):

    @property
    def latitude(self):
        st = self.data
        return float(st[st.index('(')+1:st.index(' ')])

    @property
    def longitude(self):
        st = self.data
        return float(st[st.index(' ')+1:len(st)-1])

    def __nonzero__(self):
        return bool(self.data)


geoalchemy2.Geometry = Geometry
geoalchemy2.WKTElement = WKTElement


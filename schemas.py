from app import ma

class VerbSchema(ma.Schema):
    class Meta:
        fields = ("category", "infinitif", "participe_passe", "fps_ip",\
        "sps_ip", "tps_ip", "fpp_ip", "spp_ip", "tpp_ip", "fps_ii", "sps_ii",\
        "tps_ii", "fpp_ii", "spp_ii", "tpp_ii")

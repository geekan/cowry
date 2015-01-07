#define OFPACTS                                                         \
    /* Output. */                                                       \
    OFPACT(OUTPUT,          ofpact_output,      ofpact, "output")       \
    OFPACT(GROUP,           ofpact_group,       ofpact, "group")        \
    OFPACT(CONTROLLER,      ofpact_controller,  ofpact, "controller")   \
    OFPACT(ENQUEUE,         ofpact_enqueue,     ofpact, "enqueue")      \
    OFPACT(OUTPUT_REG,      ofpact_output_reg,  ofpact, "output_reg")   \
    OFPACT(BUNDLE,          ofpact_bundle,      slaves, "bundle")       \
                                                                        \
    /* Header changes. */                                               \
    OFPACT(SET_FIELD,       ofpact_set_field,   ofpact, "set_field")    \
    OFPACT(SET_VLAN_VID,    ofpact_vlan_vid,    ofpact, "set_vlan_vid") \
    OFPACT(SET_VLAN_PCP,    ofpact_vlan_pcp,    ofpact, "set_vlan_pcp") \
    OFPACT(STRIP_VLAN,      ofpact_null,        ofpact, "strip_vlan")   \
    OFPACT(PUSH_VLAN,       ofpact_null,        ofpact, "push_vlan")    \
    OFPACT(SET_ETH_SRC,     ofpact_mac,         ofpact, "mod_dl_src")   \
    OFPACT(SET_ETH_DST,     ofpact_mac,         ofpact, "mod_dl_dst")   \
    OFPACT(SET_IPV4_SRC,    ofpact_ipv4,        ofpact, "mod_nw_src")   \
    OFPACT(SET_IPV4_DST,    ofpact_ipv4,        ofpact, "mod_nw_dst")   \
    OFPACT(SET_IP_DSCP,     ofpact_dscp,        ofpact, "mod_nw_tos")   \
    OFPACT(SET_IP_ECN,      ofpact_ecn,         ofpact, "mod_nw_ecn")   \
    OFPACT(SET_IP_TTL,      ofpact_ip_ttl,      ofpact, "mod_nw_ttl")   \
    OFPACT(SET_L4_SRC_PORT, ofpact_l4_port,     ofpact, "mod_tp_src")   \
    OFPACT(SET_L4_DST_PORT, ofpact_l4_port,     ofpact, "mod_tp_dst")   \
    OFPACT(REG_MOVE,        ofpact_reg_move,    ofpact, "move")         \
    OFPACT(STACK_PUSH,      ofpact_stack,       ofpact, "push")         \
    OFPACT(STACK_POP,       ofpact_stack,       ofpact, "pop")          \
    OFPACT(DEC_TTL,         ofpact_cnt_ids,     cnt_ids, "dec_ttl")     \
    OFPACT(SET_MPLS_LABEL,  ofpact_mpls_label,  ofpact, "set_mpls_label") \
    OFPACT(SET_MPLS_TC,     ofpact_mpls_tc,     ofpact, "set_mpls_tc")  \
    OFPACT(SET_MPLS_TTL,    ofpact_mpls_ttl,    ofpact, "set_mpls_ttl") \
    OFPACT(DEC_MPLS_TTL,    ofpact_null,        ofpact, "dec_mpls_ttl") \
    OFPACT(PUSH_MPLS,       ofpact_push_mpls,   ofpact, "push_mpls")    \
    OFPACT(POP_MPLS,        ofpact_pop_mpls,    ofpact, "pop_mpls")     \
                                                                        \
    /* Metadata. */                                                     \
    OFPACT(SET_TUNNEL,      ofpact_tunnel,      ofpact, "set_tunnel")   \
    OFPACT(SET_QUEUE,       ofpact_queue,       ofpact, "set_queue")    \
    OFPACT(POP_QUEUE,       ofpact_null,        ofpact, "pop_queue")    \
    OFPACT(FIN_TIMEOUT,     ofpact_fin_timeout, ofpact, "fin_timeout")  \
                                                                        \
    /* Flow table interaction. */                                       \
    OFPACT(RESUBMIT,        ofpact_resubmit,    ofpact, "resubmit")     \
    OFPACT(LEARN,           ofpact_learn,       specs, "learn")         \
                                                                        \
    /* Arithmetic. */                                                   \
    OFPACT(MULTIPATH,       ofpact_multipath,   ofpact, "multipath")    \
                                                                        \
    /* Other. */                                                        \
    OFPACT(NOTE,            ofpact_note,        data, "note")           \
    OFPACT(EXIT,            ofpact_null,        ofpact, "exit")         \
    OFPACT(SAMPLE,          ofpact_sample,      ofpact, "sample")       \
                                                                        \
    /* Instructions. */                                                 \
    OFPACT(METER,           ofpact_meter,       ofpact, "meter")        \
    OFPACT(CLEAR_ACTIONS,   ofpact_null,        ofpact, "clear_actions") \
    OFPACT(WRITE_ACTIONS,   ofpact_nest,        ofpact, "write_actions") \
    OFPACT(WRITE_METADATA,  ofpact_metadata,    ofpact, "write_metadata") \
    OFPACT(GOTO_TABLE,      ofpact_goto_table,  ofpact, "goto_table")

#define OFPACT(ENUM, STRUCT, MEMBER, NAME)                              \
    BUILD_ASSERT_DECL(offsetof(struct STRUCT, ofpact) == 0);            \
                                                                        \
    enum { OFPACT_##ENUM##_RAW_SIZE                                     \
           = (offsetof(struct STRUCT, MEMBER)                           \
              ? offsetof(struct STRUCT, MEMBER)                         \
              : sizeof(struct STRUCT)) };                               \
                                                                        \
    enum { OFPACT_##ENUM##_SIZE                                         \
           = ROUND_UP(OFPACT_##ENUM##_RAW_SIZE, OFPACT_ALIGNTO) };      \
                                                                        \
    static inline struct STRUCT *                                       \
    ofpact_get_##ENUM(const struct ofpact *ofpact)                      \
    {                                                                   \
        ovs_assert(ofpact->type == OFPACT_##ENUM);                      \
        return ALIGNED_CAST(struct STRUCT *, ofpact);                   \
    }                                                                   \
                                                                        \
    static inline struct STRUCT *                                       \
    ofpact_put_##ENUM(struct ofpbuf *ofpacts)                           \
    {                                                                   \
        return ofpact_put(ofpacts, OFPACT_##ENUM,                       \
                          OFPACT_##ENUM##_RAW_SIZE);                    \
    }                                                                   \
                                                                        \
    static inline void                                                  \
    ofpact_init_##ENUM(struct STRUCT *ofpact)                           \
    {                                                                   \
        ofpact_init(&ofpact->ofpact, OFPACT_##ENUM,                     \
                    OFPACT_##ENUM##_RAW_SIZE);                          \
    }
OFPACTS
#undef OFPACT

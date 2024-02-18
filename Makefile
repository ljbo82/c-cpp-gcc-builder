include core/include/functions.mk

$(info FN_REVERSE(Bora baea minha porra): $(call FN_REVERSE,Bora baea minha porra))
$(info )

testVal := LINUX-ARM-V7
$(info FN_HOST_FACTORIZE($(testVal),-,/): $(call FN_HOST_FACTORIZE,$(testVal),-,/))
$(info FN_HOST_FACTORIZE($(testVal),-): $(call FN_HOST_FACTORIZE,$(testVal),-))
$(info FN_HOST_FACTORIZE($(testVal)): $(call FN_HOST_FACTORIZE,$(testVal)))
$(info )

testVal := arduino-avr-uno
$(info FN_REVERSE(FN_HOST_FACTORIZE($(testVal),-,/)): $(call FN_REVERSE,$(call FN_HOST_FACTORIZE,$(testVal),-,/)))
$(info )

define setter
$(eval setter_v1 += $(1))
$(eval setter_v2 += $(2))
endef
$(call setter,aa,bb)
$(info setter_v1: $(setter_v1))
$(info setter_v2: $(setter_v2))
$(info )

$(info FN_NUMBER_CMP(2,2): $(call FN_NUMBER_CMP,2,2))
$(info FN_NUMBER_CMP(2,1): $(call FN_NUMBER_CMP,2,1))
$(info FN_NUMBER_CMP(1,2): $(call FN_NUMBER_CMP,1,2))
$(info )

$(info FN_SEMVER_CMP(4.2.1, 3.8.0): $(call FN_SEMVER_CMP,4.2.1,3.8.0))
$(info FN_SEMVER_CMP(3.8.0, 4.2.1): $(call FN_SEMVER_CMP,3.8.0,4.2.1))
$(info FN_SEMVER_CMP(4.0.0, 4.2.1): $(call FN_SEMVER_CMP,4.0.0,4.2.1))
$(info FN_SEMVER_CMP(4.2.1, 4.0.0): $(call FN_SEMVER_CMP,4.2.1,4.0.0))
$(info FN_SEMVER_CMP(4.2.1, 4.2.1): $(call FN_SEMVER_CMP,4.2.1,4.2.1))
$(info FN_SEMVER_CMP(4.2.1,): $(call FN_SEMVER_CMP,4.2.1,))
$(info FN_SEMVER_CMP(,4.2.1): $(call FN_SEMVER_CMP,,4.2.1,))
$(info )

override cpb_builder_mk_min_make_version := 4.0
cpb_builder_mk_make_version := $(word 3,$(shell $(MAKE) --version | grep "GNU Make"))
cpb_builder_mk_make_version_cmp := $(call FN_SEMVER_CMP,$(cpb_builder_mk_make_version),$(cpb_builder_mk_min_make_version))
$(call FN_CHECK_WORDS,cpb_builder_mk_make_version_cmp,0 1,Incompatible GNU Make version: $(if $(cpb_builder_mk_make_version),$(cpb_builder_mk_make_version),unknown) (min version is $(cpb_builder_mk_min_make_version)))

testVal = ..1.2.0
$(info FN_TOKEN($(testVal),.,1): $(call FN_TOKEN,$(testVal),.,1))
$(info FN_TOKEN($(testVal),.,2): $(call FN_TOKEN,$(testVal),.,2))
$(info FN_TOKEN($(testVal),.,3): $(call FN_TOKEN,$(testVal),.,3))
$(info FN_TOKEN($(testVal),.,4): $(call FN_TOKEN,$(testVal),.,4))
$(info FN_TOKEN($(testVal),.,5): $(call FN_TOKEN,$(testVal),.,5))
$(info )

testVal := gcc-linux-x64
$(info layers: $(call FN_FACTORIZE,$(cpb_include_toolchains_mk_host),-,/))

$(error bye)

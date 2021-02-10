library('here')

library('tidyverse')

## import data
df_input <- read_csv(
  here::here("output", "input_simple.csv"), 
  col_types = cols(
    patient_id = col_integer(),
    stp = col_character()
  )
)

# count STP for each registered patient
df_stppop = df_input %>% count(stp, name='registered')

plot_stppop_bar <- df_stppop %>%
  mutate(
    name = forcats::fct_reorder(stp, registered, median, .desc=FALSE)
  ) %>%
  ggplot() +
  geom_col(aes(x=registered/1000000, y=name, fill=registered), colour='black') +
  scale_fill_gradient(limits = c(0,NA), low="white", high="blue", guide=FALSE)+
  labs(
    title="TPP-registered patients per STP",
    subtitle= "as at 1 January 2020",
    y=NULL,
    x="Registered patients\n(million)",
    fill = NULL)+
  theme_minimal()+
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor.y = element_blank(),
    plot.title.position = "plot",
    plot.caption.position =  "plot"
  )
plot_stppop_bar


















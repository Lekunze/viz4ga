import * as React from 'react';
import {Heading, Select, TextInput} from 'grommet';
import ParamBox from "./ParamBox";

export interface TimeBudgetProps {
    timeBudget: string
    mutation: string
    crossover: string
    population: string
    setTimeBudget: (timeBudget: string) => void;
    setCrossover: (crossover: string) => void;
    setMutation: (mutation: string) => void;
    setPopulation: (population: string) => void;

}

export default class TimeBudget extends React.Component<TimeBudgetProps, {}>{
    constructor(props: TimeBudgetProps) {
        super(props);
    }

    setTimeBudget = (timeBudget) => {
        this.props.setTimeBudget(timeBudget);
    }

    setMutation = (mutation) => {
        this.props.setMutation(mutation);
    }

    setCrossover = (crossover) => {
        this.props.setCrossover(crossover);
    }

    setPopulation = (population) => {
        this.props.setPopulation(population);
    }


    render() {
        const { timeBudget, crossover, mutation, population } =  this.props;

        return(
            <ParamBox>
                <Heading level={5} margin="none"> Population Size</Heading>
                <TextInput
                    placeholder={"Enter number of generations"}
                    value={ population }
                    onChange = {event => this.setPopulation(event.target.value)}
                />

                <Heading level={5} margin="none"> Generations</Heading>
                <TextInput
                    placeholder={"Enter number of generations"}
                    value={ timeBudget }
                    onChange = {event => this.setTimeBudget(event.target.value)}
                />
                <Heading level={5} margin="none"> Mutation Probability</Heading>
                <TextInput
                    placeholder={"Enter mutation probability"}
                    value={ mutation }
                    onChange = {event => this.setMutation(event.target.value)}
                />
                <Heading level={5} margin="none"> Crossover Probability</Heading>
                <TextInput
                    placeholder={"Enter crossover probability"}
                    value={ crossover }
                    onChange = {event => this.setCrossover(event.target.value)}
                />
            </ParamBox>
        );
    }


}

